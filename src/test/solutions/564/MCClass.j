.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static lcm(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
.var 2 is z I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	iload_0
	iload_1
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_1
	iconst_2
	imul
	istore_2
	goto Label2
Label3:
	iload_0
	iconst_2
	imul
	istore_2
Label2:
Label6:
	iload_2
	iload_0
	iload_1
	imul
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	iload_2
	iload_0
	irem
	iconst_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	iload_2
	iload_1
	irem
	iconst_0
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	iand
	ifle Label11
	iload_2
	goto Label1
	goto Label10
Label11:
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label7:
	iload_0
	iload_1
	imul
	goto Label1
Label1:
	ireturn
.limit stack 11
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	bipush 20
	invokestatic MCClass/lcm(II)I
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
