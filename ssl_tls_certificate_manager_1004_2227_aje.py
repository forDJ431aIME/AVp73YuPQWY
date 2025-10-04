# 代码生成时间: 2025-10-04 22:27:55
# ssl_tls_certificate_manager.py
# This script manages SSL/TLS certificates using Python and Kivy framework.

import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

"""
    Functions related to SSL/TLS certificate management.
"""

def create_key_pair(key_size=2048):
    """Generates a new RSA key pair."""
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
    )


def create_self_signed_certificate(key_pair, subject):
    """Creates a self-signed certificate."""
    subject = x509.Name(subject)
    builder = x509.CertificateBuilder()
    builder = builder.subject_name(subject)
    builder = builder.issuer_name(subject)
    builder = builder.public_key(key_pair.public_key())
    builder = builder.serial_number(x509.random_serial_number())
    builder = builder.not_valid_before(datetime.datetime.utcnow())
    builder = builder.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
    return builder.sign(key_pair, hashes.SHA256(), default_backend())

"""
    Kivy App for managing SSL/TLS certificates.
"""
class SSLTLSCertificateManagerApp(App):
    def build(self):
        # Create the root layout
        layout = BoxLayout(orientation='vertical')

        # Create a label for instructions
        instructions_label = Label(text="Please select a private key file to manage your SSL/TLS certificates.")
        layout.add_widget(instructions_label)

        # Create a file chooser for selecting the private key file
        self.file_chooser = FileChooserListView(select_multiple=False, rootpath=os.getcwd())
        layout.add_widget(self.file_chooser)

        # Create a button to create a new certificate
        create_cert_button = Button(text='Create Certificate')
        create_cert_button.bind(on_press=self.create_certificate)
        layout.add_widget(create_cert_button)

        return layout

    def create_certificate(self, instance):
        """Handles the creation of a new SSL/TLS certificate."""
        # Get the selected private key file path
        selected_file = self.file_chooser.selection
        if not selected_file:
            self.show_error("No file selected.")
            return

        # Load the private key
        try:
            with open(selected_file[0], 'rb') as key_file:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                )
        except Exception as e:
            self.show_error(f"Failed to load private key: {str(e)}")
            return

        # Generate a self-signed certificate
        try:
            subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, u'localhost')])
            certificate = create_self_signed_certificate(private_key, subject)
            certificate_pem = certificate.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.Format.SubjectPublicKeyInfo,
            )

            # Save the certificate to a file
            with open(selected_file[0].replace('.key', '.crt'), 'wb') as cert_file:
                cert_file.write(certificate_pem)

            self.show_message("Certificate created successfully.")
        except Exception as e:
            self.show_error(f"Failed to create certificate: {str(e)}")

    def show_error(self, message):
        """Displays an error message to the user."""
        # Implement error display using Kivy's Popup or similar
        pass

    def show_message(self, message):
        """Displays a message to the user."""
        # Implement message display using Kivy's Popup or similar
        pass

"""
    Entry point of the application.
"""
if __name__ == '__main__':
    SSLTLSCertificateManagerApp().run()
