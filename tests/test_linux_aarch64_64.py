

import unittest
import cpuinfo
import helpers


class DataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'aarch64'

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def has_dmesg():
		return False

	@staticmethod
	def has_cpufreq_info():
		return False

	@staticmethod
	def has_sestatus():
		return False

	@staticmethod
	def has_sysctl():
		return False

	@staticmethod
	def has_isainfo():
		return False

	@staticmethod
	def has_kstat():
		return False

	@staticmethod
	def has_sysinfo():
		return False

	@staticmethod
	def has_lscpu():
		return True

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = '''
processor       : 90
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0

processor       : 91
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0

processor       : 92
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0

processor       : 93
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0

processor       : 94
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0

processor       : 95
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0


'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = '''
Architecture:          aarch64
Byte Order:            Little Endian
CPU(s):                96
On-line CPU(s) list:   0-95
Thread(s) per core:    1
Core(s) per socket:    48
Socket(s):             2
NUMA node(s):          2
L1d cache:             32K
L1i cache:             78K
L2 cache:              16384K
NUMA node0 CPU(s):     0-47
NUMA node1 CPU(s):     48-95
'''


class TestLinuxAarch64(unittest.TestCase):
	'''
	Make sure calls that should not return something,
	and calls that should not work return None.
	'''
	def test_all(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

		info = cpuinfo.get_cpu_info_from_registry()
		self.assertEqual(None, info)

		info = cpuinfo.get_cpu_info_from_proc_cpuinfo()
		self.assertEqual(None, info)

		info = cpuinfo.get_cpu_info_from_sysctl()
		self.assertEqual(None, info)

		info = cpuinfo.get_cpu_info_from_kstat()
		self.assertEqual(None, info)

		info = cpuinfo.get_cpu_info_from_dmesg()
		self.assertEqual(None, info)

		info = cpuinfo.get_cpu_info_from_sysinfo()
		self.assertEqual(None, info)

		info = cpuinfo.get_cpu_info_from_cpuid()
		self.assertEqual(None, info)

	'''
	This should return None on ARM, because /proc/cpuinfo returns
	useless info on ARM. It only returns good info on X86.
	'''
	def test_get_cpu_info_from_proc_cpuinfo(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

		info = cpuinfo.get_cpu_info_from_proc_cpuinfo()

		self.assertEqual(None, info)

	def test_get_cpu_info(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

		info = cpuinfo.get_cpu_info()

		#FIXME: Make sure a valid result is returned
