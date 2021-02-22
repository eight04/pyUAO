pyUAO
=====

.. image:: https://github.com/eight04/pyUAO/actions/workflows/test.yml/badge.svg
    :target: https://github.com/eight04/pyUAO/actions/workflows/test.yml
    
Big5-UAO table in pure Python.

純 Python 的 UAO (Unicode-At-On) encoder/decoder。

Installation
------------

::

  pip install uao

Usage
-----

.. code:: python

  from uao import register_uao
  register_uao() # register big5-uao as a builtin codecs
  print("无法被Big5編碼の字串♥".encode("big5-uao").decode("big5-uao"))
  
Or use the standalone ``Big5UAOCodec`` class:

.. code:: python

  from uao import Big5UAOCodec
  uao = Big5UAOCodec()
  print(uao.decode(uao.encode("无法被Big5編碼の字串♥")))
      
Changelog
---------

* 0.2.0 (Feb 22, 2021)

  - Add: support python 3.7~3.9.

* 0.1.1 (Jun 11, 2018)

  - Fix: remove a print statement.

* 0.1.0 (Jun 11, 2018)

  - First release.
