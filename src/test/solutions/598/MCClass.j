.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static isTriangle(III)Z
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	iload_2
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_0
	iload_2
	iadd
	iload_1
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	iload_1
	iload_2
	iadd
	iload_0
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	goto Label1
Label1:
	ireturn
.limit stack 8
.limit locals 3
.end method

.method public static isRightAngledTriangle(III)Z
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
.var 3 is x Z from Label0 to Label1
	iconst_0
	istore_3
Label0:
	iload_3
	iload_0
	iload_0
	imul
	iload_1
	iload_1
	imul
	iadd
	iload_2
	iload_2
	imul
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ior
	istore_3
	iload_3
	iload_0
	iload_0
	imul
	iload_2
	iload_2
	imul
	iadd
	iload_1
	iload_1
	imul
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	istore_3
	iload_3
	iload_1
	iload_1
	imul
	iload_2
	iload_2
	imul
	iadd
	iload_0
	iload_0
	imul
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ior
	istore_3
	iload_3
	goto Label1
Label1:
	ireturn
.limit stack 9
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
	iconst_3
	istore_1
.var 2 is b I from Label0 to Label1
	iconst_4
	istore_2
.var 3 is c I from Label0 to Label1
	iconst_5
	istore_3
Label0:
	iload_1
	iload_2
	iload_3
	invokestatic MCClass/isRightAngledTriangle(III)Z
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
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
