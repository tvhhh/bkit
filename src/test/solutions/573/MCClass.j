.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static isTrue(Z)Z
.var 0 is x Z from Label0 to Label1
Label0:
	iload_0
	ifle Label3
	iconst_1
	goto Label1
	goto Label2
Label3:
	iconst_0
	goto Label1
Label2:
Label1:
	ireturn
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	invokestatic MCClass/isTrue(Z)Z
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 8
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
