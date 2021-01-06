.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo([I)[I
.var 0 is a [I from Label0 to Label1
Label0:
	aload_0
	iconst_0
	aload_0
	iconst_0
	iaload
	iconst_0
	iadd
	iastore
	aload_0
	goto Label1
Label1:
	areturn
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	aload_1
	iconst_0
	bipush 6
	iastore
	aload_1
	invokestatic MCClass/foo([I)[I
	iconst_1
	bipush 7
	iastore
	iconst_0
	istore_2
	goto Label6
Label2:
	iconst_1
	iload_2
	iadd
	istore_2
Label6:
	iload_2
	iconst_5
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	aload_1
	iload_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label3:
Label1:
	return
.limit stack 6
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
