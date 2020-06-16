const koa = require('koa');
const router = require('koa-router')();
const bodyParser = require('koa-bodyparser');
const apiRouter = require('./router');

const app = new koa();

const index = router.get('/', ctx => {
    ctx.response.body = 'hi kevin';
}).routes();

const fs = require('fs');
const login = router.get('/login', ctx => {
    ctx.response.type = 'html';
    ctx.response.body = fs.createReadStream('./demos/login.html');
}).routes();

app.use(login);
app.use(index);
app.use(bodyParser());
app.use(apiRouter.routes());

app.listen(3000);

// socket , event , callback , api
