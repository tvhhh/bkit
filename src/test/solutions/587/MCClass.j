.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static getEnergy(II)[I
.var 0 is m I from Label0 to Label1
.var 1 is f I from Label0 to Label1
.var 2 is c I from Label0 to Label1
	iconst_3
	istore_2
.var 3 is res [I from Label0 to Label1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	astore_3
Label0:
	aload_3
	iconst_0
	iload_0
	iload_2
	imul
	iload_2
	imul
	iastore
	aload_3
	iconst_1
	iload_1
	bipush 8
	iadd
	bipush 8
	iadd
	iastore
	aload_3
	goto Label1
Label1:
	areturn
.limit stack 4
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is e [I from Label0 to Label1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	astore_1
Label0:
	iconst_1
	bipush 10
	ineg
	invokestatic MCClass/getEnergy(II)[I
	astore_1
	aload_1
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc "e"
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
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
