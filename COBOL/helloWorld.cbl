000001 identification division.
000002 program-id. "HELLOWORLD".
000003 author. PEGGY FISHER.
000004* cobc -x helloWorld.cbl
000005
000006 environment division.
000007
000008 data division.
000009
000010 procedure division.
000011 go to 0100-START-HERE.
000012 0100-START-HERE.
000013     display 'hello world!'.
000014     stop run.
000015 end program HELLOWORLD.
