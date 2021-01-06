.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static getBooleanMyself(Z)Z
.var 0 is n Z from Label0 to Label1
Label0:
	iload_0
	iconst_1
	iand
	goto Label1
Label1:
	ireturn
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	invokestatic MCClass/getBooleanMyself(Z)Z
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
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
