.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static isSquare(I)Z
.var 0 is n I from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_1
	istore_1
Label0:
	iload_0
	iconst_1
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
Label2:
	iconst_1
	istore_1
	goto Label10
Label6:
	iconst_1
	iload_1
	iadd
	istore_1
Label10:
	iload_1
	iload_0
	iconst_2
	idiv
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	iload_1
	iload_1
	imul
	iload_0
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label12
	iconst_1
	goto Label1
	goto Label11
Label12:
Label11:
	goto Label6
Label7:
	iconst_0
	goto Label1
Label1:
	ireturn
.limit stack 13
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 24
	invokestatic MCClass/isSquare(I)Z
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
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
