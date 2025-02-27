===============
Pyhackrf2 HTime
===============

Pyhackrf2 HTime is an extension of
`Pyhackrf2 <https://github.com/eizemazal/pyhackrf2>`_,
a Python wrapper for the C API (library libhackrf) for the HackRF One,
the open-hardware/open-source SDR by
`Great Scott Gadgets <https://www.greatscottgadgets.com/hackrf/one/>`_.

Pyhackrf2 HTime adds access to the
`HTime extension <https://github.com/fabriziop/hackrf-htime>`_
functionalities of HackRF One firmware.

The HTime extension provides the HackRF SDR with the
capability to perform timed commands and a precise phase synchronization
of internal clocks (sampling, MCU, output) for the best timing performance.


Features
~~~~~~~~

    * Unix-like time scale, with a resolution of 5 ns
    * RX/TX sampling synchronized with the time scale
    * Fine time scale/frequency adjust for synchronization with remote reference
      radio signals with a resolution of about 0.25 Hz @ 10 MHz
    * No external hardware required


For now, Pyhackrf2 HTime works only with a 10 MHz sample rate.


Linux Build and Install
~~~~~~~~~~~~~~~~~~~~~~~

Recent versions of Linux distributions do not allow the installation of python
packages at system level. A python virtual environment is needed.

1. Install libhackrf, see
   `HackRF HTime <https://github.com/fabriziop/hackrf-htime>`_

2. Create a python virtual environment

.. code::

  python -m venv <path_to_new_virtual_environment>

2. Activate the python virtual environment

.. code::

  . <path_to_new_virtual_environment>/bin/activate

3. Install package build into the python environment

.. code::

  pip install build

4. Build PyhackRF_HTime

.. code::

  cd <pyhackrf2_htime_root_dir>
  python -m build

5. Install PyhackRF HTime into the python environment

.. code::

  pip install dist/pyhackrf2_htime-1.0.3.tar.gz


Examples
~~~~~~~~

Please, see the :doc:`set_host_time example <set_host_time>`


Pyhackrf2 HTime API
~~~~~~~~~~~~~~~~~~~

This API allows access to all the firmware features of HTime.
The API is almost all implemented as
`Python properties <https://docs.python.org/3/howto/descriptor.html>`_
of the class HackRF. So, the first
step to use this API is to instantiate an HackRF object. For example,

.. code::

  from pyhackrf2_htime import HackRF
  hackrf = HackRF()

Then the HackRF properties by Pyhackrf2 HTime can be written or read,
as for example,

.. code::

  # set second counter to 1000
  hackrf.seconds = 1000

  # read second counter value in seconds variable
  seconds = hackrf.seconds


Pyhackrf2 HTime API Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: apientry

  hackrf.reset()

Reset the HackRF device. This is a normal python function, not a property.


.. rst-class:: apientry

  id = hackrf.get_board_id()

Get the **id** (str) of the HackRF board. This is a normal python function,
not a property.


.. rst-class:: apientry

  status = hackrf.clkin_status

Get the **status** value (uint8_t) of the input clock. If true, an input clock
is present and valid for device synchronization.


.. rst-class:: apientry

  hackrf.hw_sync_mode = enable

Set the **enable** value (uint8_t) for the hardware synchronization mode.
If true, the A/D sampling is started by the trigger hardware signal. It is
a level trigger and must be kept on for all the sampling time.


.. rst-class:: apientry

  hackrf.divisor = divisor


Set the **divisor** value (uint32_t) into the ticks counter at the next PPS.
With the HackRF MCU working @ 200 MHz, the ticks counter must be set to
200000000-1 to obtain a counting period of 1 second.


.. rst-class:: apientry

  hackrf.divisor_one_pps = divisor

Set the **divisor** value (uint32_t) into the ticks counter from the next PPS for
only one counter cycle then restore the previous divisor value.


.. rst-class:: apientry

  hackrf.trig_delay_next_pps = trig_delay

Set the **trig_delay** value (uint32_t) as the sampling trigger delay at the
next PPS. The trigger delay is from the start of the second (PPS leading edge)
in tick units.

 
.. rst-class:: apientry

  seconds = hackrf.seconds

Get the value of the second counter immediately into **seconds** (int64_t).

  
.. rst-class:: apientry

  hackrf.seconds = seconds

Set the **seconds** value (int64_t) immediately into the second counter.


.. rst-class:: apientry

  hackrf.seconds_next_pps = seconds

Set the **seconds** value (int64_t) at the next PPS into the second counter.

  
.. rst-class:: apientry

  ticks = hackrf.ticks

Get the value of the tick counter immediately into **ticks** (uint32_t).

  
.. rst-class:: apientry

  hackrf.ticks = ticks

Set the **ticks** value (uint32_t) immediately into the tick counter.

  
.. rst-class:: apientry

  hackrf.clk_freq = clk_freq

Set the **clk_freq** value (double) as the sampling rate synchronized to the MCU
clock. Must be a value near (+-100 Hz) 10 MHz.


.. rst-class:: apientry

  hackrf.mcu_clk_sync = enable

Set the **enable** value (uint8_t) of the MCU synchronized clock mode.
When this mode is on, all relevant clocks are kept in sync to avoid phase shifts
and frequency drifts.


.. raw:: html

 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><span property="dct:title">Pyhackrf2 HTime documentation</span> by <span property="cc:attributionName">Fabrizio Pollastri</span> is licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>

