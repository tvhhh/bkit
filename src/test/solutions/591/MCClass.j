.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static getCubeVolume(F)F
.var 0 is s F from Label0 to Label1
Label0:
	fload_0
	fload_0
	fmul
	fload_0
	fmul
	goto Label1
Label1:
	freturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is s F from Label0 to Label1
	ldc 5.0
	fstore_1
.var 2 is v F from Label0 to Label1
	ldc 0.0
	fstore_2
Label0:
	fload_1
	invokestatic MCClass/getCubeVolume(F)F
	fstore_2
	fload_2
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 3
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
