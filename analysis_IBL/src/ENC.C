{
//=========Macro generated from canvas: module_canvas_s/
//=========  (Fri May 30 18:43:00 2014) by ROOT version5.34/01
   TCanvas *module_canvas_s = new TCanvas("module_canvas_s", "",-1,1,954,565);
   module_canvas_s->SetHighLightColor(2);
   module_canvas_s->Range(81.75,-11.15625,269.25,100.4063);
   module_canvas_s->SetFillColor(0);
   module_canvas_s->SetBorderMode(0);
   module_canvas_s->SetBorderSize(2);
   module_canvas_s->SetFrameBorderMode(0);
   module_canvas_s->SetFrameBorderMode(0);
   
   THStack *noise_distribution = new THStack();
   noise_distribution->SetName("noise_distribution");
   noise_distribution->SetTitle("ENC distributions");
   
   TH1F *noise_distribution_stack_1 = new TH1F("noise_distribution_stack_1","ENC distributions",50,100.5,250.5);
   noise_distribution_stack_1->SetMinimum(0);
   noise_distribution_stack_1->SetMaximum(89.25);
   noise_distribution_stack_1->SetDirectory(0);
   noise_distribution_stack_1->SetStats(0);

   Int_t ci;   // for color index setting
   ci = TColor::GetColor("#000099");
   noise_distribution_stack_1->SetLineColor(ci);
   noise_distribution_stack_1->GetXaxis()->SetTitle("Equivalent Noise Charge");
   noise_distribution_stack_1->GetXaxis()->SetLabelFont(42);
   noise_distribution_stack_1->GetXaxis()->SetLabelSize(0.035);
   noise_distribution_stack_1->GetXaxis()->SetTitleSize(0.035);
   noise_distribution_stack_1->GetXaxis()->SetTitleFont(42);
   noise_distribution_stack_1->GetYaxis()->SetTitle("Number of FE/3#e^-");
   noise_distribution_stack_1->GetYaxis()->SetLabelFont(42);
   noise_distribution_stack_1->GetYaxis()->SetLabelSize(0.035);
   noise_distribution_stack_1->GetYaxis()->SetTitleSize(0.035);
   noise_distribution_stack_1->GetYaxis()->SetTitleFont(42);
   noise_distribution_stack_1->GetZaxis()->SetLabelFont(42);
   noise_distribution_stack_1->GetZaxis()->SetLabelSize(0.035);
   noise_distribution_stack_1->GetZaxis()->SetTitleSize(0.035);
   noise_distribution_stack_1->GetZaxis()->SetTitleFont(42);
   noise_distribution->SetHistogram(noise_distribution_stack_1);
   
   
   TH1D *noisemeanvalue_Planar = new TH1D("noisemeanvalue_Planar","noisemeanvalue_Planar",50,100.5,250.5);
   noisemeanvalue_Planar->SetBinContent(1,1);
   noisemeanvalue_Planar->SetBinContent(2,1);
   noisemeanvalue_Planar->SetBinContent(4,6);
   noisemeanvalue_Planar->SetBinContent(5,32);
   noisemeanvalue_Planar->SetBinContent(6,62);
   noisemeanvalue_Planar->SetBinContent(7,72);
   noisemeanvalue_Planar->SetBinContent(8,85);
   noisemeanvalue_Planar->SetBinContent(9,75);
   noisemeanvalue_Planar->SetBinContent(10,59);
   noisemeanvalue_Planar->SetBinContent(11,33);
   noisemeanvalue_Planar->SetBinContent(12,22);
   noisemeanvalue_Planar->SetBinContent(13,10);
   noisemeanvalue_Planar->SetBinContent(14,4);
   noisemeanvalue_Planar->SetBinContent(15,2);
   noisemeanvalue_Planar->SetBinContent(16,2);
   noisemeanvalue_Planar->SetBinContent(25,1);
   noisemeanvalue_Planar->SetEntries(467);

   ci = TColor::GetColor("#0000ff");
   noisemeanvalue_Planar->SetFillColor(ci);
   noisemeanvalue_Planar->SetFillStyle(3002);

   ci = TColor::GetColor("#000099");
   noisemeanvalue_Planar->SetLineColor(ci);
   noisemeanvalue_Planar->GetXaxis()->SetLabelFont(42);
   noisemeanvalue_Planar->GetXaxis()->SetLabelSize(0.035);
   noisemeanvalue_Planar->GetXaxis()->SetTitleSize(0.035);
   noisemeanvalue_Planar->GetXaxis()->SetTitleFont(42);
   noisemeanvalue_Planar->GetYaxis()->SetLabelFont(42);
   noisemeanvalue_Planar->GetYaxis()->SetLabelSize(0.035);
   noisemeanvalue_Planar->GetYaxis()->SetTitleSize(0.035);
   noisemeanvalue_Planar->GetYaxis()->SetTitleFont(42);
   noisemeanvalue_Planar->GetZaxis()->SetLabelFont(42);
   noisemeanvalue_Planar->GetZaxis()->SetLabelSize(0.035);
   noisemeanvalue_Planar->GetZaxis()->SetTitleSize(0.035);
   noisemeanvalue_Planar->GetZaxis()->SetTitleFont(42);
   noise_distribution->Add(noisemeanvalue_Planar,"");
   
   TH1D *noisemeanvalue_FBK = new TH1D("noisemeanvalue_FBK","noisemeanvalue_FBK",50,100.5,250.5);
   noisemeanvalue_FBK->SetBinContent(13,1);
   noisemeanvalue_FBK->SetBinContent(14,2);
   noisemeanvalue_FBK->SetBinContent(15,2);
   noisemeanvalue_FBK->SetBinContent(16,9);
   noisemeanvalue_FBK->SetBinContent(17,9);
   noisemeanvalue_FBK->SetBinContent(18,15);
   noisemeanvalue_FBK->SetBinContent(19,11);
   noisemeanvalue_FBK->SetBinContent(20,4);
   noisemeanvalue_FBK->SetBinContent(21,3);
   noisemeanvalue_FBK->SetBinContent(22,5);
   noisemeanvalue_FBK->SetBinContent(24,2);
   noisemeanvalue_FBK->SetBinContent(25,4);
   noisemeanvalue_FBK->SetBinContent(26,3);
   noisemeanvalue_FBK->SetBinContent(28,1);
   noisemeanvalue_FBK->SetBinContent(29,1);
   noisemeanvalue_FBK->SetBinContent(30,1);
   noisemeanvalue_FBK->SetBinContent(46,1);
   noisemeanvalue_FBK->SetBinContent(47,1);
   noisemeanvalue_FBK->SetEntries(75);

   ci = TColor::GetColor("#ff0000");
   noisemeanvalue_FBK->SetFillColor(ci);
   noisemeanvalue_FBK->SetFillStyle(3004);

   ci = TColor::GetColor("#000099");
   noisemeanvalue_FBK->SetLineColor(ci);
   noisemeanvalue_FBK->GetXaxis()->SetLabelFont(42);
   noisemeanvalue_FBK->GetXaxis()->SetLabelSize(0.035);
   noisemeanvalue_FBK->GetXaxis()->SetTitleSize(0.035);
   noisemeanvalue_FBK->GetXaxis()->SetTitleFont(42);
   noisemeanvalue_FBK->GetYaxis()->SetLabelFont(42);
   noisemeanvalue_FBK->GetYaxis()->SetLabelSize(0.035);
   noisemeanvalue_FBK->GetYaxis()->SetTitleSize(0.035);
   noisemeanvalue_FBK->GetYaxis()->SetTitleFont(42);
   noisemeanvalue_FBK->GetZaxis()->SetLabelFont(42);
   noisemeanvalue_FBK->GetZaxis()->SetLabelSize(0.035);
   noisemeanvalue_FBK->GetZaxis()->SetTitleSize(0.035);
   noisemeanvalue_FBK->GetZaxis()->SetTitleFont(42);
   noise_distribution->Add(noisemeanvalue_FBK,"");
   
   TH1D *noisemeanvalue_CNM = new TH1D("noisemeanvalue_CNM","noisemeanvalue_CNM",50,100.5,250.5);
   noisemeanvalue_CNM->SetBinContent(7,3);
   noisemeanvalue_CNM->SetBinContent(9,3);
   noisemeanvalue_CNM->SetBinContent(10,3);
   noisemeanvalue_CNM->SetBinContent(11,2);
   noisemeanvalue_CNM->SetBinContent(12,7);
   noisemeanvalue_CNM->SetBinContent(13,8);
   noisemeanvalue_CNM->SetBinContent(14,11);
   noisemeanvalue_CNM->SetBinContent(15,7);
   noisemeanvalue_CNM->SetBinContent(16,4);
   noisemeanvalue_CNM->SetBinContent(17,3);
   noisemeanvalue_CNM->SetBinContent(18,6);
   noisemeanvalue_CNM->SetBinContent(19,8);
   noisemeanvalue_CNM->SetBinContent(20,7);
   noisemeanvalue_CNM->SetBinContent(21,1);
   noisemeanvalue_CNM->SetBinContent(22,2);
   noisemeanvalue_CNM->SetBinContent(23,4);
   noisemeanvalue_CNM->SetBinContent(26,1);
   noisemeanvalue_CNM->SetEntries(80);

   ci = TColor::GetColor("#006600");
   noisemeanvalue_CNM->SetFillColor(ci);
   noisemeanvalue_CNM->SetFillStyle(3005);

   ci = TColor::GetColor("#000099");
   noisemeanvalue_CNM->SetLineColor(ci);
   noisemeanvalue_CNM->GetXaxis()->SetLabelFont(42);
   noisemeanvalue_CNM->GetXaxis()->SetLabelSize(0.035);
   noisemeanvalue_CNM->GetXaxis()->SetTitleSize(0.035);
   noisemeanvalue_CNM->GetXaxis()->SetTitleFont(42);
   noisemeanvalue_CNM->GetYaxis()->SetLabelFont(42);
   noisemeanvalue_CNM->GetYaxis()->SetLabelSize(0.035);
   noisemeanvalue_CNM->GetYaxis()->SetTitleSize(0.035);
   noisemeanvalue_CNM->GetYaxis()->SetTitleFont(42);
   noisemeanvalue_CNM->GetZaxis()->SetLabelFont(42);
   noisemeanvalue_CNM->GetZaxis()->SetLabelSize(0.035);
   noisemeanvalue_CNM->GetZaxis()->SetTitleSize(0.035);
   noisemeanvalue_CNM->GetZaxis()->SetTitleFont(42);
   noise_distribution->Add(noisemeanvalue_CNM,"");
   noise_distribution->Draw("nostack");
   
   TPaveText *pt = new TPaveText(0.3615789,0.94,0.6384211,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *text = pt->AddText("ENC distributions");
   pt->Draw();
   
   TLegend *leg = new TLegend(0.1,0.1,0.3,0.2,NULL,"brNDC");
   leg->SetBorderSize(1);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("noisemeanvalue_Planar","Planar CiS","F");

   ci = TColor::GetColor("#0000ff");
   entry->SetFillColor(ci);
   entry->SetFillStyle(3002);

   ci = TColor::GetColor("#000099");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("noisemeanvalue_FBK","3D FBK","F");

   ci = TColor::GetColor("#ff0000");
   entry->SetFillColor(ci);
   entry->SetFillStyle(3004);

   ci = TColor::GetColor("#000099");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("noisemeanvalue_CNM","3D CNM","F");

   ci = TColor::GetColor("#006600");
   entry->SetFillColor(ci);
   entry->SetFillStyle(3005);

   ci = TColor::GetColor("#000099");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   leg->Draw();
      tex = new TLatex(0.12,0.8,"ATLAS");
tex->SetNDC();
   tex->SetTextFont(72);
   tex->SetTextSize(0.07);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.28,0.8,"Internal");
tex->SetNDC();
   tex->SetTextFont(42);
   tex->SetTextSize(0.07);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.65,0.7,"ENC after loading");
tex->SetNDC();
   tex->SetTextFont(42);
   tex->SetLineWidth(2);
   tex->Draw();
   module_canvas_s->Modified();
   module_canvas_s->cd();
   module_canvas_s->SetSelected(module_canvas_s);
}
