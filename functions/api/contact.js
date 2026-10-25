export async function onRequestPost({request,env}) {
  const headers={"Content-Type":"application/json; charset=utf-8","Cache-Control":"no-store"};
  const reply=(status,data)=>new Response(JSON.stringify(data),{status,headers});
  const origin=request.headers.get("Origin");
  if(origin){let host;try{host=new URL(origin).hostname}catch{return reply(403,{error:"origin"})}if(!["simetrika-7wr.pages.dev","simetrika.lu","www.simetrika.lu"].includes(host)&&!host.endsWith(".simetrika.pages.dev"))return reply(403,{error:"origin"});}
  if(Number(request.headers.get("content-length")||0)>12000)return reply(413,{error:"size"});
  let data;try{data=await request.json()}catch{return reply(400,{error:"invalid_json"})}
  if(!data||typeof data!=="object")return reply(400,{error:"invalid_data"});
  const value=(key,max)=>typeof data[key]==="string"?data[key].trim().slice(0,max+1):"";
  const name=value("name",150),email=value("email",254),phone=value("phone",80),project=value("project",5000),website=value("website",100),lang=value("lang",8);
  if(website)return reply(200,{ok:true});
  if(!name||name.length>150||!project||project.length>5000||(!email&&!phone)||email.length>254||phone.length>80)return reply(400,{error:"validation"});
  if(email&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))return reply(400,{error:"email"});
  const endpoint=env.FORMSPREE_ENDPOINT;
  if(!endpoint||!/^https:\/\/formspree\.io\/f\/[a-zA-Z0-9]+$/.test(endpoint))return reply(503,{error:"not_configured"});
  try{
    const res=await fetch(endpoint,{method:"POST",headers:{"Accept":"application/json","Content-Type":"application/json"},body:JSON.stringify({name,email,phone,project,_subject:"Nouvelle demande Simetrika",language:lang||"fr"})});
    if(!res.ok)return reply(502,{error:"delivery_failed"});
    return reply(200,{ok:true});
  }catch{return reply(502,{error:"delivery_failed"})}
}
