.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo(F)F
.var 0 is n F from Label0 to Label1
Label0:
	fload_0
	ldc 2.0
	fcmpl
	iconst_0
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	ldc 2.0
	goto Label1
	goto Label2
Label3:
	fload_0
	goto Label1
Label2:
Label1:
	freturn
.limit stack 6
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
	ldc 0.0
	fstore_1
Label0:
	ldc 5.0
	invokestatic MCClass/foo(F)F
	fstore_1
	fload_1
	invokestatic io/string_of_float(F)Ljava/lang/String;
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
