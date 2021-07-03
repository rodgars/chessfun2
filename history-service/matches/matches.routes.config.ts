import { CommonRoutesConfig } from "../common/common.routes.config";
import express from 'express';

export class MatchesRoutes extends CommonRoutesConfig{
    configureRoutes(): express.Application {
        this.app.route('/history/:userName')
            .get((req: express.Request, res: express.Response) => {
                res.status(200).send(`GET requested for username ${req.params.userName}`)
            })
        return this.app;
    }

    constructor(app: express.Application){
        super(app, 'MatchesRoutes');
    }
}
