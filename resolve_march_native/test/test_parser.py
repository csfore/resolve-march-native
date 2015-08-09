# Copyright (C) 2015 Sebastian Pipping <sebastian@pipping.org>
# Licensed under GPL v2 or later

from unittest import TestCase

from resolve_march_native.parser import extract_flags


class TestParser(TestCase):
	_EXPECTED_FLAGS_WESTMERE_NATIVE = [
		# options passed
		'-march=westmere',
		'-mmmx',
		'-mno-3dnow',
		'-msse',
		'-msse2',
		'-msse3',
		'-mssse3',
		'-mno-sse4a',
		'-mcx16',
		'-msahf',
		'-mno-movbe',
		'-maes',
		'-mno-sha',
		'-mpclmul',
		'-mpopcnt',
		'-mno-abm',
		'-mno-lwp',
		'-mno-fma',
		'-mno-fma4',
		'-mno-xop',
		'-mno-bmi',
		'-mno-bmi2',
		'-mno-tbm',
		'-mno-avx',
		'-mno-avx2',
		'-msse4.2',
		'-msse4.1',
		'-mno-lzcnt',
		'-mno-rtm',
		'-mno-hle',
		'-mno-rdrnd',
		'-mno-f16c',
		'-mno-fsgsbase',
		'-mno-rdseed',
		'-mno-prfchw',
		'-mno-adx',
		'-mfxsr',
		'-mno-xsave',
		'-mno-xsaveopt',
		'-mno-avx512f',
		'-mno-avx512er',
		'-mno-avx512cd',
		'-mno-avx512pf',
		'-mno-prefetchwt1',
		'--param l1-cache-size=32',
		'--param l1-cache-line-size=64',
		'--param l2-cache-size=12288',
		'-mtune=westmere',
		'-fverbose-asm',
		'-fstack-protector-strong',

		# options enabled
		'-faggressive-loop-optimizations',
		'-fasynchronous-unwind-tables',
		'-fauto-inc-dec',
		'-fcommon',
		'-fdelete-null-pointer-checks',
		'-fdwarf2-cfi-asm',
		'-fearly-inlining',
		'-feliminate-unused-debug-types',
		'-fexceptions',
		'-ffunction-cse',
		'-fgcse-lm',
		'-fgnu-runtime',
		'-fgnu-unique',
		'-fident',
		'-finline-atomics',
		'-fira-hoist-pressure',
		'-fira-share-save-slots',
		'-fira-share-spill-slots',
		'-fivopts',
		'-fkeep-static-consts',
		'-fleading-underscore',
		'-flifetime-dse',
		'-fmath-errno',
		'-fmerge-debug-strings',
		'-fpeephole',
		'-fprefetch-loop-arrays',
		'-freg-struct-return',
		'-fsched-critical-path-heuristic',
		'-fsched-dep-count-heuristic',
		'-fsched-group-heuristic',
		'-fsched-interblock',
		'-fsched-last-insn-heuristic',
		'-fsched-rank-heuristic',
		'-fsched-spec',
		'-fsched-spec-insn-heuristic',
		'-fsched-stalled-insns-dep',
		'-fshow-column',
		'-fsigned-zeros',
		'-fsplit-ivs-in-unroller',
		'-fstack-protector-strong',
		'-fstrict-volatile-bitfields',
		'-fsync-libcalls',
		'-ftrapping-math',
		'-ftree-coalesce-vars',
		'-ftree-cselim',
		'-ftree-forwprop',
		'-ftree-loop-if-convert',
		'-ftree-loop-im',
		'-ftree-loop-ivcanon',
		'-ftree-loop-optimize',
		'-ftree-parallelize-loops=',
		'-ftree-phiprop',
		'-ftree-reassoc',
		'-ftree-scev-cprop',
		'-funit-at-a-time',
		'-funwind-tables',
		'-fverbose-asm',
		'-fzero-initialized-in-bss',
		'-m128bit-long-double',
		'-m64',
		'-m80387',
		'-maes',
		'-malign-stringops',
		'-mavx256-split-unaligned-load',
		'-mavx256-split-unaligned-store',
		'-mcx16',
		'-mfancy-math-387',
		'-mfp-ret-in-387',
		'-mfxsr',
		'-mglibc',
		'-mieee-fp',
		'-mlong-double-80',
		'-mmmx',
		'-mpclmul',
		'-mpopcnt',
		'-mpush-args',
		'-mred-zone',
		'-msahf',
		'-msse',
		'-msse2',
		'-msse3',
		'-msse4',
		'-msse4.1',
		'-msse4.2',
		'-mssse3',
		'-mtls-direct-seg-refs',
	]

	def test_parse_westmere_native_s(self):
		with open('resolve_march_native/test/data/westmere--4-9-3-gentoo--native.s', 'r') as f:
			received_flags = list(extract_flags(f.read()))

		self.assertEquals(received_flags, self._EXPECTED_FLAGS_WESTMERE_NATIVE)
