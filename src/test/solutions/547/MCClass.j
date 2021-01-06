.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static swap([I)V
.var 0 is a [I from Label0 to Label1
.var 1 is tmp I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	aload_0
	iconst_0
	iaload
	istore_1
	aload_0
	iconst_0
	aload_0
	iconst_1
	iaload
	iastore
	aload_0
	iconst_1
	iload_1
	iastore
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [I from Label0 to Label1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	astore_1
Label0:
	aload_1
	invokestatic MCClass/swap([I)V
	aload_1
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
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
