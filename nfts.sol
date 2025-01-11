// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CertificationNFT is ERC721, Ownable {
    uint256 public tokenCounter;

    struct Certification {
        string productName;
        string certificateDetails;
        uint256 waterFootprint;
        string issuedBy;
    }

    mapping(uint256 => Certification) public certifications;

    constructor() ERC721("CertificationNFT", "CERT") {
        tokenCounter = 0;
    }

    // Function to mint a new NFT certificate
    function issueCertificate(
        address recipient,
        string memory productName,
        string memory certificateDetails,
        uint256 waterFootprint,
        string memory issuedBy
    ) public onlyOwner {
        uint256 newTokenId = tokenCounter;
        _safeMint(recipient, newTokenId);

        certifications[newTokenId] = Certification({
            productName: productName,
            certificateDetails: certificateDetails,
            waterFootprint: waterFootprint,
            issuedBy: issuedBy
        });

        tokenCounter++;
    }

    // Function to view certification details
    function getCertificationDetails(uint256 tokenId)
        public
        view
        returns (
            string memory productName,
            string memory certificateDetails,
            uint256 waterFootprint,
            string memory issuedBy
        )
    {
        Certification memory cert = certifications[tokenId];
        return (
            cert.productName,
            cert.certificateDetails,
            cert.waterFootprint,
            cert.issuedBy
        );
    }
}
