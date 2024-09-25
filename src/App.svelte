<script>
  import QR from "./lib/QR.svelte";
  import collections from "./assets/collections.json";
  let selectedIndex = Math.round(collections.length/2);

  const clamp = (num, a, b) =>
    Math.max(Math.min(num, Math.max(a, b)), Math.min(a, b));

  let loaderTimer;

  let hiResImg;
  let lowResImg;

  const loadHiRes = () => {
    hiResImg.src = `https://bpldcassets.blob.core.windows.net/derivatives/images/${t.exemplary_image_ssi}/image_access_800.jpg`;
    hiResImg.addEventListener("load", () => {
      hiResImg.style.display = "block";
      lowResImg.style.display = "none";
    });
  };

  const handleChange = (e) => {
    if ([37, 39, 82].includes(e.which)) {
      hiResImg.style.display = "none";
      lowResImg.style.display = "block";
      clearTimeout(loaderTimer);

      let newI = e.which === 37 ? selectedIndex - 1 : e.which === 39 ? selectedIndex + 1 : Math.floor(Math.random() * (collections.length));
      selectedIndex = clamp(
        newI,
        0,
        collections.length - 1,
      );
      loaderTimer = setTimeout(loadHiRes, 1000);
    }
  };

  const getCollectionByScroll = (s) => {
    let index = s ? clamp(s, 0, collections.length - 1) : 0;
    return collections[index];
  };

  $: t = getCollectionByScroll(selectedIndex);
</script>

<svelte:window on:keydown={handleChange} />

<main>
  <div id="img-holder">
    <img id="hires-img" bind:this={hiResImg} alt="Collection thumbnail" />
    <img
      id="thumb-img"
      bind:this={lowResImg}
      src={`./thumbnails/${t.exemplary_image_ssi.replace(":", "__")}.jpg`}
      alt="Collection thumbnail"
    />
  </div>
  <div id="label-bar">
    <div id="title">{t.title_info_primary_tsi}, {t.date_tsim}</div>
    <div id="qr"><QR url={`https://collections.leventhalmap.org/search/${t.id}`} /></div>
  </div>
  <div id="top-section">
    <div id="date">{t.date_start_dtsi.substring(0,4)}</div>
    <div id="slider-holder"><input type="range" min="0" max={collections.length-1} bind:value={selectedIndex} id="slider"></div>
  </div>

</main>

<style>
  main {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    top: 0;
    background-color: black;
  }

  #img-holder {
    position: absolute;
    left: 5%;
    top: 10%;
    right: 5%;
    bottom: 10%;
  }

  #hires-img {
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: none;
  }

  #thumb-img {
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  #label-bar {
    position: absolute;
    bottom: 0;
    width: 100%;
    display: flex;
    align-items: flex-end;
    flex-direction: row;
    font-weight: 800;
  }

  #date {
    font-size: 2.2em;
    font-weight: 900;
  }

  #title {
    font-size: 1.2em;
    flex-grow: 2;
    padding: 20px;
    text-align: left;
  }

  #qr { 
    padding: 10px;
  }


  #top-section {
    position: absolute;
    top: 0;
    width: 100%;
    background-color: #222;
    display: flex;
    flex-direction: row;
  }

  #top-section > div {
    padding: 10px;
  }


  #slider-holder {
    flex-grow: 2;
  }

  #slider { width: 100%; margin-top: 18px; }



</style>
