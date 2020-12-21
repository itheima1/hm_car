#ifdef  LABEL
#define extern
#endif

#define mylog(format,...) printf(format"\r\n",##__VA_ARGS__) extern
