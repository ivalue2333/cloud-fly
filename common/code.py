CodeNum = 10 ** 4


ErrorCodeNotError = 0
ErrorCodeSystem = 1
ErrorCodeParamWrong = 2

ErrorCodeAuthAlreadySignUp = CodeNum + 1
ErrorCodeAuthNotSignUp = CodeNum + 2
ErrorCodeAuthNotAuth = CodeNum + 3
ErrorCodeAuthNotSignIn = CodeNum + 4

ErrorCodeMongoValidate = 2 * CodeNum + 1
ErrorCodeMongoCreate = 2 * CodeNum + 2
ErrorCodeMongoOperate = 2 * CodeNum + 3


ErrorCodeMap = {
    ErrorCodeNotError: "ok",
    ErrorCodeSystem: "system error",
    ErrorCodeParamWrong: "params parser error",

    ErrorCodeAuthAlreadySignUp: "name already sign up",
    ErrorCodeAuthNotSignUp: "name and password not sign up",
    ErrorCodeAuthNotAuth: "name and password auth error",
    ErrorCodeAuthNotSignIn: "please sign in",

    ErrorCodeMongoValidate: "mongo validate error",
    ErrorCodeMongoCreate: "mongo create error",
    ErrorCodeMongoOperate: "mongo operate error"
}
