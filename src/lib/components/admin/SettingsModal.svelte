<script>
	import { getContext } from 'svelte';
	import Modal from '../common/Modal.svelte';
	import Database from './Settings/Database.svelte';

	import General from './Settings/General.svelte';
	import Users from './Settings/Users.svelte';

	import Banners from '$lib/components/admin/Settings/Banners.svelte';
	import { toast } from 'svelte-sonner';
	import Pipelines from './Settings/Pipelines.svelte';

	const i18n = getContext('i18n');

	export let show = false;

	let selectedTab = 'general';
</script>