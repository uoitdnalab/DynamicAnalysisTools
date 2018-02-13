/*
 * Adapted from: https://gist.github.com/arq5x/5315739
*/

#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <zlib.h>

#define RUN_COUNT 500000

int main(int argc, char* argv[])
{
	int i;
	for (i = 0; i < RUN_COUNT; i++)
	{
		
		char a[50] = "Hello world. Compress this!";
		
		char b[50];
		
		char c[50];
		
		//Compress a into b
		z_stream defstream;
		defstream.zalloc = Z_NULL;
		defstream.zfree = Z_NULL;
		defstream.opaque = Z_NULL;
		
		defstream.avail_in = (uInt)strlen(a)+1;
		defstream.next_in = (Bytef *)a;
		defstream.avail_out = (uInt)sizeof(b);
		defstream.next_out = (Bytef *)b;
		
		//Run the compression
		deflateInit(&defstream, Z_BEST_COMPRESSION);
		deflate(&defstream, Z_FINISH);
		deflateEnd(&defstream);
		
		//Decompress b into c
		z_stream infstream;
		infstream.zalloc = Z_NULL;
		infstream.zfree = Z_NULL;
		infstream.opaque = Z_NULL;
		
		infstream.avail_in = (uInt)((char*)defstream.next_out - b);
		infstream.next_in = (Bytef *)b;
		infstream.avail_out = (uInt)sizeof(c);
		infstream.next_out = (Bytef *)c;
		
		//Run the decompression
		inflateInit(&infstream);
		inflate(&infstream, Z_NO_FLUSH);
		inflateEnd(&infstream);
		
		//make sure uncompressed is exactly equal to original
		assert(strcmp(a,c) == 0);
	}
}
