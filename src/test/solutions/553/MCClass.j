.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static factorial(I)I
.var 0 is n I from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is i I from Label0 to Label1
	iconst_1
	istore_2
Label0:
Label2:
	iconst_1
	ifle Label3
	iload_2
	iconst_1
	iadd
	istore_2
	iload_1
	iload_2
	imul
	istore_1
	iload_2
	iload_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	iload_1
	goto Label1
	goto Label4
Label5:
Label4:
	goto Label2
Label3:
	iload_1
	goto Label1
Label1:
	ireturn
.limit stack 5
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	bipush 10
	istore_1
Label0:
	iload_1
	invokestatic MCClass/factorial(I)I
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
