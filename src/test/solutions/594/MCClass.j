.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static getCylinderVolume(FF)F
.var 0 is r F from Label0 to Label1
.var 1 is h F from Label0 to Label1
.var 2 is pi F from Label0 to Label1
	ldc 3.14
	fstore_2
Label0:
	fload_2
	fload_0
	fmul
	fload_0
	fmul
	fload_1
	fmul
	goto Label1
Label1:
	freturn
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is r F from Label0 to Label1
	ldc 3.0
	fstore_1
.var 2 is h F from Label0 to Label1
	ldc 4.0
	fstore_2
.var 3 is v F from Label0 to Label1
	ldc 0.0
	fstore_3
Label0:
	fload_1
	fload_2
	invokestatic MCClass/getCylinderVolume(FF)F
	fstore_3
	fload_3
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
