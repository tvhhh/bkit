.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static exp(II)I
.var 0 is a I from Label0 to Label1
.var 1 is n I from Label0 to Label1
.var 2 is x I from Label0 to Label1
	iconst_1
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	iconst_0
	istore_3
	goto Label6
Label2:
	iconst_1
	iload_3
	iadd
	istore_3
Label6:
	iload_3
	iload_1
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_2
	iload_0
	imul
	istore_2
	goto Label2
Label3:
	iload_2
	goto Label1
Label1:
	ireturn
.limit stack 6
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	iconst_3
	invokestatic MCClass/exp(II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
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
