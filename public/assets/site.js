(function(){
  var form=document.getElementById('lead'); if(!form) return;
  var sel=document.getElementById('need'), st=document.getElementById('status'), btn=form.querySelector('button');
  document.querySelectorAll('[data-need]').forEach(function(a){
    a.addEventListener('click',function(){ sel.value=a.getAttribute('data-need'); });
  });
  var q=new URLSearchParams(location.search).get('need'); if(q){ sel.value=q; }
  form.addEventListener('submit',async function(ev){
    ev.preventDefault(); st.className='status';
    var data=new FormData(form); data.append('page',location.pathname);
    data.append('_subject','Website lead: '+sel.options[sel.selectedIndex].text);
    btn.disabled=true; var t=btn.textContent; btn.textContent='Sending…';
    try{
      var r=await fetch('https://formspree.io/f/mvzekrgq',{method:'POST',body:data,headers:{'Accept':'application/json'}});
      if(!r.ok) throw new Error('send failed');
      form.reset(); st.className='status ok';
      st.textContent='Thanks, it’s with us. You’ll get a reply from shei@manacreators.com, usually within a day.';
      btn.textContent='Sent';
    }catch(err){
      st.className='status err';
      st.textContent='That didn’t send. Please email shei@manacreators.com directly.';
      btn.disabled=false; btn.textContent=t;
    }
  });
})();
