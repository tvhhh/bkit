.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static factorial(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label4
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
	iload_0
	iconst_1
	isub
	invokestatic MCClass/factorial(I)I
	imul
	goto Label1
Label2:
Label1:
	ireturn
.limit stack 6
.limit locals 1
.end method

.method public static combination(II)I
.var 0 is n I from Label0 to Label1
.var 1 is r I from Label0 to Label1
Label0:
	iload_0
	invokestatic MCClass/factorial(I)I
	iload_1
	invokestatic MCClass/factorial(I)I
	iload_0
	iload_1
	isub
	invokestatic MCClass/factorial(I)I
	imul
	idiv
	goto Label1
Label1:
	ireturn
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	bipush 10
	istore_1
.var 2 is y I from Label0 to Label1
	iconst_5
	istore_2
Label0:
	iload_1
	iload_2
	invokestatic MCClass/combination(II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
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
