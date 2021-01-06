.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static f(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iload_0
	imul
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 1
.end method

.method public static g(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iload_0
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 1
.end method

.method public static compose(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	invokestatic MCClass/g(I)I
	invokestatic MCClass/f(I)I
	goto Label1
Label1:
	ireturn
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_3
	istore_1
Label0:
	iload_1
	invokestatic MCClass/compose(I)I
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
