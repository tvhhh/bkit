.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo([[II)[I
.var 0 is a [[I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	aload_0
	iconst_0
	aaload
	iconst_0
	iconst_1
	iastore
	aload_0
	iload_1
	aaload
	goto Label1
Label1:
	areturn
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is a [[I from Label0 to Label1
	iconst_2
	multianewarray [[I 1
	dup
	iconst_0
	iconst_3
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
	dup
	iconst_2
	iconst_3
	iastore
	pop
	dup
	iconst_1
	iconst_3
	newarray int
	aastore
	dup
	iconst_1
	aaload
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	pop
	astore_2
.var 3 is x [I from Label0 to Label1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	astore_3
Label0:
	aload_2
	iload_1
	invokestatic MCClass/foo([[II)[I
	astore_3
	aload_3
	iconst_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
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
