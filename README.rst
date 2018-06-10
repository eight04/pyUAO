pyUAO
=====

.. image:: https://travis-ci.org/eight04/pyUAO.svg?branch=master
    :target: https://travis-ci.org/eight04/pyUAO
    
Big5-UAO table in pure Python.

純 Python 的 UAO (Unicode-At-On) encoder/decoder。

Installation
------------

::

  pip install uao

Usage
-----

.. code:: python

  import uao
  uao.register() # register big5-uao as a builtin codecs
  print("无法被Big5編碼の字串♥".encode("big5-uao").decode("big5-uao"))
  
Or use the standalone ``Big5UAOCodec`` class:

.. code:: python

  from uao import Big5UAOCodecs
  uao = Big5UAOCodecs()
  print(uao.decode(uao.encode("无法被Big5編碼の字串♥")))
      
Changelog
---------

* 0.1.0 (Next)

  - First release.
