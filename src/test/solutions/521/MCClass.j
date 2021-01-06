.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static fibonacci(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_1
	goto Label1
	goto Label2
Label3:
	iload_0
	iconst_2
	isub
	invokestatic MCClass/fibonacci(I)I
	iload_0
	iconst_1
	isub
	invokestatic MCClass/fibonacci(I)I
	iadd
	goto Label1
Label2:
Label1:
	ireturn
.limit stack 6
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	bipush 6
	istore_1
Label0:
	iload_1
	invokestatic MCClass/fibonacci(I)I
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
