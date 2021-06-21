<template>
  <div class="pageContainer">
    <div class = "paragraphContainer">
        <h1 id ="sectionTitle">What is the COVID-19 vaccine?</h1>
        <p class = "Ptext">The COVID-19 vaccine is a microRNA based Vaccine which means that it uses a piece of RNA to generate immunity 
            toward the SARS-CoV-2 virus (the Virus that causes COVID-19). Your body is made of individual cells which each perform different processes.
            These processes are carried out by small molecules known as proteins. The protiens in your cells don't last forever, and you must make new ones.
            Every cell in your body contains a set of instructionsfor making every single protein, known as DNA. Because the DNA contains instructions for every
            protein, each time a new protein needs to be made your body only needs the information for that specific protein. Thus, that segment of your DNA
            will be turned into RNA, a smaller set of instructions that can be used to create the protein. Below is a diagram showing this process:</p>
        <img src="../assets/Central-Dogma.jpg"/>
        <p class="Ptext">The COVID-19 vaccine uses RNA for a part of the SARS-CoV-2 virus. When the vaccine is injected into your body, 
            your immune cells will pick up the RNA and create the protein that it codes for. Then these proteins can be used by other immune cells to 
            learn what the diseaes will look like and create antibodies, which are molecules that bind to another specific partner moleucle marking it
            for your immune system to fight off. So the mRNA vaccine esentually allows us to prepare our immune system for the disease. The video below shows a visual example
            of how mRNA vaccines work:</p>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/WOvvyqJ-vwo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    <div class = "paragraphContainer">
        <h1 id="sectionTitle">Are these vaccines safe?</h1>
        <p class='Ptext'>Yes! mRNA vaccines, like the COVID-19 vaccine are actually safter than the vaccines we current get. Vaccines that we are currently given
            come in two types: killed vaccines and live-attenuated vaccines. Killed vaccines inject a dead form of the diease or virus into your system, so that
            our immune system can train itself. Live-attenuated vaccines inject an altered, but still live, form of the diease/pathogen into your system. While both off
            these vaccines are safe, there is still a small risk that the diease/virus may not be dead or fully altered. In an mRNA vaccine, you are only exposed to a PART of 
            the disease/virus. So, there is no chance of the diseaes/virus coming alive in your system.</p>
        <p class='Ptext'>Beceause mRNA vaccines are safer and we can design what RNA are given, mRNA vaccines can be used to fight a range of
            diseases that we previously could not create vaccines for. These include viruses like ebola or zika as well as cancer</p>
        <p class='Ptext'>There have also been recent concerns that the COVID-19 virus has affected sperm count in men, but a recent study has shown no effect:</p>
        <a href="https://www.urologytimes.com/view/study-shows-covid-19-vaccines-do-not-affect-male-fertility">Lay Audience Article</a>
        <br>
        <a href="https://jamanetwork.com/journals/jama/fullarticle/2781360">Scientific Article</a>
  </div>
  <div class="paragraphContainer">
      <h1 id='sectionTitle'>Resources:</h1>
      <p>1. <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6446947/">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6446947/</a></p>
      <p>2. <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7745181/">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7745181/</a></p>
  </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.sectionTitle {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 25;

}

.pageContainer {
    width: 100%;
    vertical-align: center;
}

.paragraphContainer {
    background-color: rgb(209, 208, 208);
    left: 15%;
    width: 70%;
    position: relative;
    border-radius: 2px;
    box-shadow: 1px 2px 2px rgb(43, 43, 43); 
    padding: 0px 5px 5px 5px;
}
.Ptext {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 12;
    text-align: left;
}
</style>