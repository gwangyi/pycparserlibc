defines = [
    "NULL	0",
    "BUFSIZ		1024",
    "FOPEN_MAX	20",
    "FILENAME_MAX	1024",
    "SEEK_SET	0",
    "SEEK_CUR	1",
    "SEEK_END	2",
    "__LITTLE_ENDIAN 1234",
    "LITTLE_ENDIAN __LITTLE_ENDIAN",
    "__BIG_ENDIAN 4321",
    "BIG_ENDIAN __BIG_ENDIAN",
    "__BYTE_ORDER __LITTLE_ENDIAN",
    "BYTE_ORDER __BYTE_ORDER",
    "EXIT_FAILURE 1",
    "EXIT_SUCCESS 0",
    "UCHAR_MAX 255",
    "USHRT_MAX 65535",
    "UINT_MAX 4294967295U",
    "RAND_MAX 32767",
    "INT_MAX 32767",
    "__bool_true_false_are_defined 1",
    "false 0",
    "true 1",
    "va_start(_ap, _type) __builtin_va_start((_ap))",
    "va_arg(_ap, _type) __builtin_va_arg((_ap))",
    "va_end(_list)",
]

typedefs = r"""
typedef int size_t;
typedef int __builtin_va_list;
typedef int __gnuc_va_list;
typedef int __int8_t;
typedef int __uint8_t;
typedef int __int16_t;
typedef int __uint16_t;
typedef int __int_least16_t;
typedef int __uint_least16_t;
typedef int __int32_t;
typedef int __uint32_t;
typedef int __int64_t;
typedef int __uint64_t;
typedef int __int_least32_t;
typedef int __uint_least32_t;
typedef int __s8;
typedef int __u8;
typedef int __s16;
typedef int __u16;
typedef int __s32;
typedef int __u32;
typedef int __s64;
typedef int __u64;
typedef int _LOCK_T;
typedef int _LOCK_RECURSIVE_T;
typedef int _off_t;
typedef int __dev_t;
typedef int __uid_t;
typedef int __gid_t;
typedef int _off64_t;
typedef int _fpos_t;
typedef int _ssize_t;
typedef int wint_t;
typedef int _mbstate_t;
typedef int _flock_t;
typedef int _iconv_t;
typedef int __ULong;
typedef int __FILE;
typedef int ptrdiff_t;
typedef int wchar_t;
typedef int __off_t;
typedef int __pid_t;
typedef int __loff_t;
typedef int u_char;
typedef int u_short;
typedef int u_int;
typedef int u_long;
typedef int ushort;
typedef int uint;
typedef int clock_t;
typedef int time_t;
typedef int daddr_t;
typedef int caddr_t;
typedef int ino_t;
typedef int off_t;
typedef int dev_t;
typedef int uid_t;
typedef int gid_t;
typedef int pid_t;
typedef int key_t;
typedef int ssize_t;
typedef int mode_t;
typedef int nlink_t;
typedef int fd_mask;
typedef int _types_fd_set;
typedef int clockid_t;
typedef int timer_t;
typedef int useconds_t;
typedef int suseconds_t;
typedef int FILE;
typedef int fpos_t;
typedef int cookie_read_function_t;
typedef int cookie_write_function_t;
typedef int cookie_seek_function_t;
typedef int cookie_close_function_t;
typedef int cookie_io_functions_t;
typedef int div_t;
typedef int ldiv_t;
typedef int lldiv_t;
typedef int sigset_t;
typedef int __sigset_t;
typedef int _sig_func_ptr;
typedef int sig_atomic_t;
typedef int __tzrule_type;
typedef int __tzinfo_type;
typedef int mbstate_t;
typedef int sem_t;
typedef int pthread_t;
typedef int pthread_attr_t;
typedef int pthread_mutex_t;
typedef int pthread_mutexattr_t;
typedef int pthread_cond_t;
typedef int pthread_condattr_t;
typedef int pthread_key_t;
typedef int pthread_once_t;
typedef int pthread_rwlock_t;
typedef int pthread_rwlockattr_t;
typedef int pthread_spinlock_t;
typedef int pthread_barrier_t;
typedef int pthread_barrierattr_t;
typedef int jmp_buf;
typedef int rlim_t;
typedef int sa_family_t;
typedef int sigjmp_buf;
typedef int stack_t;
typedef int siginfo_t;
typedef int z_stream;
typedef int int8_t;
typedef int uint8_t;
typedef int int16_t;
typedef int uint16_t;
typedef int int32_t;
typedef int uint32_t;
typedef int int64_t;
typedef int uint64_t;
typedef int int_least8_t;
typedef int uint_least8_t;
typedef int int_least16_t;
typedef int uint_least16_t;
typedef int int_least32_t;
typedef int uint_least32_t;
typedef int int_least64_t;
typedef int uint_least64_t;

typedef int int_fast8_t;
typedef int uint_fast8_t;
typedef int int_fast16_t;
typedef int uint_fast16_t;
typedef int int_fast32_t;
typedef int uint_fast32_t;
typedef int int_fast64_t;
typedef int uint_fast64_t;
typedef int intptr_t;
typedef int uintptr_t;
typedef int intmax_t;
typedef int uintmax_t;
typedef _Bool bool;
typedef int va_list;
typedef int __end_of_fakes__;
"""

libc_headers = [
    '_ansi.h',
    '_syslist.h',
    'alloca.h',
    'ar.h',
    'argz.h',
    'arpa',
    'asm-generic',
    'assert.h',
    'complex.h',
    'ctype.h',
    'dirent.h',
    'dlfcn.h',
    'endian.h',
    'envz.h',
    'errno.h',
    'fastmath.h',
    'fcntl.h',
    'features.h',
    'fenv.h',
    'float.h',
    'getopt.h',
    'grp.h',
    'iconv.h',
    'ieeefp.h',
    'inttypes.h',
    'iso646.h',
    'langinfo.h',
    'libgen.h',
    'libintl.h',
    'limits.h',
    'linux',
    'locale.h',
    'malloc.h',
    'math.h',
    'netdb.h',
    'netinet',
    'newlib.h',
    'openssl',
    'paths.h',
    'process.h',
    'pthread.h',
    'pwd.h',
    'reent.h',
    'regdef.h',
    'regex.h',
    'sched.h',
    'search.h',
    'semaphore.h',
    'setjmp.h',
    'signal.h',
    'stdarg.h',
    'stdbool.h',
    'stddef.h',
    'stdint.h',
    'stdio.h',
    'stdlib.h',
    'string.h',
    'sys',
    'syslog.h',
    'tar.h',
    'termios.h',
    'tgmath.h',
    'time.h',
    'unctrl.h',
    'unistd.h',
    'utime.h',
    'utmp.h',
    'wchar.h',
    'wctype.h',
    'zlib.h',
]
