import {Application} from "https://deno.land/x/oak@v11.1.0/mod.ts"
import { oakCors } from "https://deno.land/x/cors@v1.2.2/oakCors.ts";
import { Client } from "https://deno.land/x/postgres@v0.17.0/mod.ts";

const client = new Client({
    user: "postgres",
    database: "localhost",
    hostname: "localhost",
    port: 5432,
    password:"root",
  });

  

const app = new Application()
app.use(oakCors())

app.use(async ctx=> {
   
    
if (ctx.request.method !== "POST") return;
const body = ctx.request.body({ type: "json" });
const data = await body.value
    await client.connect();
  const application_no = data['application_no'];
  const name = data['name'];
  const address= data['address'];
  const internships_completed= data['internships_completed'];
  const gender= data['gender'];
  const mail_id= data['mail_id'];
  const languages_known = data['languages_known'];
  const cgpa= data['cgpa'];
  const interview_date = data['interview_date'];
  const skillset = data['skillsets'];
  

const array_result = await client.queryArray`insert into register_form values(${application_no},${name},${address},${internships_completed}, ${gender},${mail_id},${languages_known},${cgpa},${interview_date}, ${skillset})`;
console.log(array_result.rows); 

await client.end();
    ctx.response.body= {message : "successful"}
    ctx.response.status=200
})


app.listen({port:8000})
console.log("server started")



