.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static getFloatMyself(F)F
.var 0 is n F from Label0 to Label1
Label0:
	fload_0
	ldc 0.0
	fadd
	goto Label1
Label1:
	freturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 5.0
	invokestatic MCClass/getFloatMyself(F)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
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
