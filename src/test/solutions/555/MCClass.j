.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo()I
.var 0 is i I from Label0 to Label1
	iconst_0
	istore_0
Label0:
	iconst_0
	istore_0
	goto Label6
Label2:
	iconst_1
	iload_0
	iadd
	istore_0
Label6:
	iload_0
	bipush 10
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_0
	iconst_5
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	iload_0
	goto Label1
	goto Label7
Label8:
Label7:
	goto Label2
Label3:
	iload_0
	goto Label1
Label1:
	ireturn
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	invokestatic MCClass/foo()I
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
