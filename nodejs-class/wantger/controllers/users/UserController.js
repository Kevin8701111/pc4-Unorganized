class UserController {
    async login(ctx, next) {
        let name = ctx.request.body.name || '',
            pwd = ctx.request.body.pwd || '';
        console.log(name, pwd);

        ctx.body = {
            status: true,
            token: '123'
        }

    }

    async userInfo(ctx, next) {
        let data = {
            name: 'kevin',
            age: '21'
        }
        ctx.body = {
            status: true,
            data
        };
    }
    // async userEntrance(ctx, next) {
    //     let 
    // }

    }

module.exports = new UserController();