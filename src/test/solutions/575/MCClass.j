.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static canIPassThisCourse()Z
Label0:
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "Can I pass this course?"
	invokestatic io/printStrLn(Ljava/lang/String;)V
	invokestatic MCClass/canIPassThisCourse()Z
	ifle Label3
	ldc "Yes"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label3:
	ldc "Also yes"
	invokestatic io/print(Ljava/lang/String;)V
Label2:
Label1:
	return
.limit stack 1
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
