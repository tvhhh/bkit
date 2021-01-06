.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	iconst_1
	istore_1
	goto Label6
Label2:
	iconst_1
	iload_1
	iadd
	istore_1
Label6:
	iload_1
	iconst_5
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
.var 2 is j I from Label0 to Label1
	iconst_0
	istore_2
	iconst_0
	istore_2
	goto Label11
Label7:
	iconst_1
	iload_2
	iadd
	istore_2
Label11:
	iload_2
	iload_1
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	ldc "*"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label7
Label8:
	ldc "\n"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label3:
Label1:
	return
.limit stack 9
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
