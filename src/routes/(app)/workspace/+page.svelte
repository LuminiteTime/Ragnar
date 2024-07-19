<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	onMount(() => {
		window.location.href = '/workspace/documents';
	});
</script>
