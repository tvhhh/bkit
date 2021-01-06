.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static fibonacci(I)I
.var 0 is n I from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is x I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is y I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	iconst_0
	istore_1
	goto Label6
Label2:
	iconst_1
	iload_1
	iadd
	istore_1
Label6:
	iload_1
	iload_0
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_1
	iconst_0
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	iload_1
	iconst_1
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ior
	ifle Label8
	iconst_1
	istore_2
	iconst_1
	istore_3
	goto Label7
Label8:
.var 4 is z I from Label0 to Label1
	iconst_0
	istore 4
	iload_2
	istore 4
	iload_2
	iload_3
	iadd
	istore_2
	iload 4
	istore_3
Label7:
	goto Label2
Label3:
	iload_2
	goto Label1
Label1:
	ireturn
.limit stack 9
.limit locals 5
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
