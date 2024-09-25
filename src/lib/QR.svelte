<script>
    import qrcode from "qrcode";
    import { onMount } from "svelte";

    export let url;
    let qrCanvas;

    let q = null;

    onMount(() => {
        q = qrcode.toCanvas(qrCanvas, url);
    });

    $: q ? qrcode.toCanvas(qrCanvas, url, {"scale": 3}) : null;
</script>

<canvas bind:this={qrCanvas} />

<style>

    canvas { background-color: #fff; border-radius: 10px; }
    
</style>

