.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [[I from Label0 to Label1
	iconst_2
	multianewarray [[I 1
	dup
	iconst_0
	iconst_2
	newarray int
	aastore
	dup
	iconst_0
	aaload
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	pop
	dup
	iconst_1
	iconst_2
	newarray int
	aastore
	dup
	iconst_1
	aaload
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	pop
	astore_1
.var 2 is y I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	aload_1
	iconst_1
	aaload
	iconst_1
	iaload
	istore_2
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
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
