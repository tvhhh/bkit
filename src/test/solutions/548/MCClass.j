.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static getSec(III)I
.var 0 is d I from Label0 to Label1
.var 1 is h I from Label0 to Label1
.var 2 is m I from Label0 to Label1
Label0:
	bipush 60
	iload_2
	bipush 60
	iload_1
	bipush 24
	iload_0
	imul
	iadd
	imul
	iadd
	imul
	goto Label1
Label1:
	ireturn
.limit stack 6
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	iconst_1
	iconst_1
	iconst_1
	invokestatic MCClass/getSec(III)I
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 2
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
