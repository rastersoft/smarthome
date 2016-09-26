using GLib;
using Gedit;
using Peas;

namespace gedit_smarthome {

	public class GeditSmartHome : Gedit.ViewActivatable, Peas.ExtensionBase {

		public GeditSmartHome() {
			GLib.Object();
		}

		public Gedit.View view {
			owned get; construct;
		}

		public void activate () {
			this.view.smart_home_end = Gtk.SourceSmartHomeEndType.BEFORE;
		}

		public void deactivate () {
			this.view.smart_home_end = Gtk.SourceSmartHomeEndType.AFTER;
		}

/*		public void do_update_state() {
		}*/

	}
}

[ModuleInit]
public void peas_register_types (TypeModule module) {
	var objmodule = module as Peas.ObjectModule;

	// Register my plugin extension
	objmodule.register_extension_type (typeof (Gedit.ViewActivatable), typeof (gedit_smarthome.GeditSmartHome));
}
