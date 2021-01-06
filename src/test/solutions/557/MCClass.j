.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo()[Ljava/lang/String;
Label0:
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Hello"
	aastore
	dup
	iconst_1
	ldc "World"
	aastore
	dup
	iconst_2
	ldc "Again"
	aastore
	goto Label1
Label1:
	areturn
.limit stack 4
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/foo()[Ljava/lang/String;
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
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
