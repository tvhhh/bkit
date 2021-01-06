.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x I
.field static y I
.field static z I

.method public static getX()I
Label0:
	getstatic MCClass.x I
	goto Label1
Label1:
	ireturn
.limit stack 1
.limit locals 0
.end method

.method public static getY()I
Label0:
	getstatic MCClass.y I
	goto Label1
Label1:
	ireturn
.limit stack 1
.limit locals 0
.end method

.method public static getZ()I
Label0:
	getstatic MCClass.z I
	goto Label1
Label1:
	ireturn
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_0
	putstatic MCClass.x I
	iconst_0
	putstatic MCClass.y I
	iconst_0
	putstatic MCClass.z I
Label0:
	invokestatic MCClass/getX()I
	invokestatic MCClass/getY()I
	iadd
	invokestatic MCClass/getZ()I
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
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
