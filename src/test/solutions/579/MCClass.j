.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static getStringMyself(Ljava/lang/String;)Ljava/lang/String;
.var 0 is n Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "Getting "
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	invokestatic io/print(Ljava/lang/String;)V
	ldc "\n"
	invokestatic io/print(Ljava/lang/String;)V
	ldc "Successful"
	invokestatic io/printStrLn(Ljava/lang/String;)V
	aload_0
	goto Label1
Label1:
	areturn
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "Hello World"
	invokestatic MCClass/getStringMyself(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
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
