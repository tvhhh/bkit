.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	dup
	iconst_3
	iconst_3
	iastore
	dup
	iconst_4
	iconst_4
	iastore
	astore_1
.var 2 is x I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	aload_1
	aload_1
	aload_1
	aload_1
	aload_1
	iconst_0
	iaload
	invokestatic MCClass/foo(I)I
	iaload
	invokestatic MCClass/foo(I)I
	iaload
	invokestatic MCClass/foo(I)I
	iaload
	invokestatic MCClass/foo(I)I
	iaload
	istore_2
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
.limit locals 3
.end method

.method public static foo(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	iadd
	goto Label1
Label1:
	ireturn
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
